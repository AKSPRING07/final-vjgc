Get-ChildItem -Path "c:\Users\Admin\vjs-website-\public\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    # 1. Fix the "mega-4-col" attribute bug and turn it into a class
    # Old bug: class="mega-menu-content" mega-4-col
    # Target: class="mega-menu-content mega-4-col"
    $newContent = $content -replace 'class="mega-menu-content"\s+mega-4-col', 'class="mega-menu-content mega-4-col"'
    
    # 2. Add "sus-dropdown" class to the parent UL for width control
    # We find the Sustainability link and look upwards for the UL
    $sustainabilityLink = 'href="sustainability.html" role="button"'
    if ($newContent.Contains($sustainabilityLink)) {
        $linkIndex = $newContent.IndexOf($sustainabilityLink)
        # Find the UL before this link (the one with dropdown-menu class)
        $ulIndex = $newContent.LastIndexOf('class="dropdown-menu"', $linkIndex)
        
        if ($ulIndex -ne -1 -and ($linkIndex - $ulIndex) -lt 500) {
             # Check if it already has sus-dropdown
             if (-not $newContent.Substring($ulIndex, 100).Contains("sus-dropdown")) {
                 # Insert class
                 $newContent = $newContent.Insert($ulIndex + 20, " sus-dropdown")
                 Write-Host "Added sus-dropdown class to $($_.Name)"
             }
        }
    }

    if ($newContent -ne $content) {
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($_.Name)"
    }
}
