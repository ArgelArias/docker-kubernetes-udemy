Set WshShell = WScript.CreateObject("WScript.Shell")
Return = WshShell.Run("py .\startOracleDocker.py", 1, false)