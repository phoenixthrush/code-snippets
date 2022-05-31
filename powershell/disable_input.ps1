#requires -RunAsAdministrator
# when run without administrator privileges, the keyboard will not be blocked!

# get access to API functions that block user input
# blocking of keyboard input requires administrator privileges
$code = @'
    [DllImport("user32.dll")]
    public static extern bool BlockInput(bool fBlockIt);
'@

$userInput = Add-Type -MemberDefinition $code -Name Blocker -Namespace UserInput -PassThru

# block user input
$null = $userInput::BlockInput($true)

# sleeping 5 seconds
Start-Sleep -Seconds 5

# unblock user input
$null = $userInput::BlockInput($false)
