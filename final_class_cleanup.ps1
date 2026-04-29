Get-ChildItem -Path "c:\Users\Admin\vjs-website-\public\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    # Fix the misplaced classes (outside quotes)
    $newContent = $content -replace 'class="mega-menu-content"\s+mega-4-col', 'class="mega-menu-content mega-4-col"'
    $newContent = $newContent -replace 'class="dropdown-menu"\s+sus-dropdown', 'class="dropdown-menu sus-dropdown"'
    
    if ($newContent -ne $content) {
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed classes in $($_.Name)"
    }
}
