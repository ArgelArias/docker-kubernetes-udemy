Set WshShell = WScript.CreateObject("WScript.Shell")
Return = WshShell.Run("py .\stopOracleDocker.py", 1, false)