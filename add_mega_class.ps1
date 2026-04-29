Get-ChildItem -Path "c:\Users\Admin\vjs-website-\public\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    # Target the Sustainability dropdown specifically
    # Find the block that has sustainability.html and mega-menu-content
    $sustainabilityLink = 'href="sustainability.html" role="button"'
    
    if ($content.Contains($sustainabilityLink)) {
        # Find the NEXT occurrence of mega-menu-content after this link
        $linkIndex = $content.IndexOf($sustainabilityLink)
        $megaIndex = $content.IndexOf('class="mega-menu-content"', $linkIndex)
        
        if ($megaIndex -ne -1 -and ($megaIndex - $linkIndex) -lt 1000) {
            # Check if it already has mega-4-col
            $existingClass = 'class="mega-menu-content mega-4-col"'
            if (-not $content.Contains($existingClass)) {
                $newContent = $content.Insert($megaIndex + 25, " mega-4-col")
                [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
                Write-Host "Added mega-4-col to $($_.Name)"
            } else {
                Write-Host "Already has mega-4-col in $($_.Name)"
            }
        }
    }
}
