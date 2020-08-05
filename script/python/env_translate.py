import pandas as pd
import sys
import os
import posixpath


def process_file(env):
    dforiginal = pd.read_csv(env, sep="=", names=["key", "value"])

    # Replace cmd path to bash path
    df = dforiginal.copy()
    df["bash_value"] = df["value"]
    df["bash_value"] = df["bash_value"].str.replace("C:", "/c")
    df["bash_value"] = df["bash_value"].str.replace("D:", "/d")
    df["bash_value"] = df["bash_value"].str.replace(r"\\", "/")
    df["bash_value"] = df["bash_value"].str.replace(r"(?<!=');(?!=')", "':'")
    df["bash_value"] = df["bash_value"].str.replace(r"[']*:[']*", "':'")
    df["bash_value"] = "'" + df["bash_value"] + "'"

    # Problematic key
    df = df[df['key'].str.match("^[\w_]+$")]
    df = df[df['key'] != "ConEmuArgs"]
    df = df[df['key'] != "PS1"] 
    df = df[df['key'] != "PROCESSOR_IDENTIFIER"]

    # output 1: full list of variable
    df_out = ("export" + " " + df["key"] + "=" + df["bash_value"]).dropna().copy()

    # Copy PATH, LIB, INCLUDE and WindowsSdkDir to new dataframe for another bash script
    df1 = df[df["key"].str.match("^(PATH|LIB|INCLUDE|WindowsSdkDir|VCToolsInstallDir)$")].copy()

    # Process PATH, LIB and INCLUDE 
    re1 = "([\w\./]*" + "(?:include|bin|lib)/[\d\.]+/" + "[\w\./]*)"
    df1["windows_sdk"] = df1["bash_value"].str.findall(
	        re1).apply(lambda x: list(set(x))).str.join(sep=":") # avoid duplicate by list set
    re2 = "([\w\./]*" + "VC/Tools/MSVC" + "[\w\./]*)"
    df1["msvc"] = df1["bash_value"].str.findall(
	        re2).apply(lambda x: list(set(x))).str.join(sep=":") # avoid duplicate by list set
    df1["full"] = df1["windows_sdk"]
    df1.loc[df1["key"] != "PATH", "full"] = (df1[df1["key"] != "PATH"]["full"] + 
	                                             ":" + df1[df1["key"] != "PATH"]["msvc"])
    df1["full"] = df1["full"].str.replace(r"[']*:[']*", "':'")
    df1["full"] = df1["full"].str.replace(r"^[']*", "'")
    df1["full"] = df1["full"].str.replace(r"[']*$", "'")
    df1["full"] = df1["full"].str.replace(r"[']+", "'")

    df1.loc[df1["key"] == "PATH", "full"] = "$PATH:" + df1[df1["key"] == "PATH"]["full"]
    
    # Copy WindowsSdkDir from the original dataframe
    df1.loc[df1["key"] == "WindowsSdkDir", "full"] = df[df["key"] == "WindowsSdkDir"]["bash_value"]

    # Copy VCToolsInstallDir from the original dataframe
    df1.loc[df1["key"] == "VCToolsInstallDir", "full"] = df[df["key"] == "VCToolsInstallDir"]["bash_value"]

    # output 2
    df1_out = ("export" + " " + df1["key"] + "=" + df1["full"]).dropna().copy()

    return df_out, df1_out



if __name__ == "__main__":
    infile = sys.argv[1]
    out1, out2 = process_file(infile)
    out1.to_csv("env_full.sh", index=False, header=False)
    out2.to_csv("env.sh", index=False, header=False)
