# Dim VarHrs

# VarHrs InputBox("Enter the approximate Execution time in Hrs")

# exptime DateAdd("h", VarHrs, Now)

# Set Wshell = WScript.CreateObject("WScript.Shell")

# While Now < exptime
# Wscript.Sleep 120000

# Wshell.SendKeys "{NUMLOCK}" Wshell.SendKeys "{NUMLOCK}"

# Wend

Dim VarHrs
Dim exptime
Dim Wshell

VarHrs = InputBox("Enter the approximate execution time in Hrs")

If IsNumeric(VarHrs) Then
    exptime = DateAdd("h", CDbl(VarHrs), Now)
    
    Set Wshell = WScript.CreateObject("WScript.Shell")
    
    While Now < exptime
        WScript.Sleep 120000
        Wshell.SendKeys "{NUMLOCK}"
        Wshell.SendKeys "{NUMLOCK}"
    Wend
Else
    MsgBox "Please enter a valid numeric value for execution time."
End If
