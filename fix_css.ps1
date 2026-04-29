$path = "c:\Users\Admin\vjs-website-\public\css\custom.css"
$content = Get-Content $path -Raw
$content = $content -replace '\.esg-card:nth-child\(1\) \.esg-icon-wrap \{ color: #9ec008; \} /\* Environmental - Green \*/', '.esg-env .esg-icon-wrap { color: #9ec008 !important; }'
$content = $content -replace '\.esg-card:nth-child\(2\) \.esg-icon-wrap \{ color: #008D96; \} /\* Social - Teal \*/', '.esg-soc .esg-icon-wrap { color: #008D96 !important; }'
$content = $content -replace '\.esg-card:nth-child\(3\) \.esg-icon-wrap \{ color: #08201b; \} /\* Governance - Dark \*/', '.esg-gov .esg-icon-wrap { color: #08201b !important; }'
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
Write-Host "CSS Fixed."
