$publicPath = "c:\Users\Admin\vjs-website-\public"
$scriptTag = "`n`t`t<script src=`"js/mega-dropdown.js`"></script>"
$themeJs = '<script src="js/theme.js"></script>'

Get-ChildItem -Path "$publicPath\*.html" | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $newContent = $content
    
    # 1. Update Sustainability link to be a toggle (href="javascript:void(0)")
    # This prevents navigation on click and allows the dropdown to open
    $oldLink = 'href="sustainability.html" role="button"'
    $newLink = 'href="javascript:void(0)" role="button"'
    $newContent = $newContent.Replace($oldLink, $newLink)
    
    # 2. Inject the script if not already there
    if ($newContent -notmatch 'mega-dropdown\.js') {
        if ($newContent -match [regex]::Escape($themeJs)) {
            $newContent = $newContent.Replace($themeJs, $themeJs + $scriptTag)
        }
    }

    if ($newContent -ne $content) {
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($_.Name)"
    }
}
