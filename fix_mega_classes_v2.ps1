Get-ChildItem -Path "c:\Users\Admin\vjs-website-\public\*.html" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $newContent = $content
    
    # 1. Fix the "mega-4-col" class if still needed (handling various spacing)
    $newContent = [regex]::Replace($newContent, 'class="mega-menu-content"\s+mega-4-col', 'class="mega-menu-content mega-4-col"')
    
    # 2. Add "sus-dropdown" class to the correct UL
    $sustainabilityLink = 'href="sustainability.html" role="button"'
    if ($newContent.Contains($sustainabilityLink)) {
        $linkIndex = $newContent.IndexOf($sustainabilityLink)
        # The UL is AFTER the link in the HTML structure
        $ulIndex = $newContent.IndexOf('class="dropdown-menu"', $linkIndex)
        
        if ($ulIndex -ne -1 -and ($ulIndex - $linkIndex) -lt 200) {
             # Check if it already has sus-dropdown
             # Check a small window around the UL tag
             $ulWindow = $newContent.Substring($ulIndex, 100)
             if (-not $ulWindow.Contains("sus-dropdown")) {
                 # Insert class
                 $newContent = $newContent.Insert($ulIndex + 21, " sus-dropdown")
                 Write-Host "Added sus-dropdown class to $($_.Name)"
             }
        }
    }

    # 3. CLEANUP: Remove internal mega menu styles that override navbar-vjs.css
    # We look for the block starting with /* ================= MEGA MENU (Businesses) ================= */
    # and remove it until the next </style> or a safe distance.
    $styleStart = $newContent.IndexOf('/* ================= MEGA MENU (Businesses) ================= */')
    if ($styleStart -ne -1) {
        # Find the next </style> tag
        $styleEnd = $newContent.IndexOf('</style>', $styleStart)
        if ($styleEnd -ne -1 -and ($styleEnd - $styleStart) -lt 5000) {
            # We want to remove the block but keep the </style> tag
            # We'll also remove the @media (min-width: 992px) { that likely wraps it if it's there
            # Actually, let's be more precise.
            
            # Find the starting @media if it's just before
            $mediaSearch = $newContent.LastIndexOf('@media (min-width: 992px) {', $styleStart)
            if ($mediaSearch -ne -1 -and ($styleStart - $mediaSearch) -lt 100) {
                $removeStart = $mediaSearch
            } else {
                $removeStart = $styleStart
            }
            
            $newContent = $newContent.Remove($removeStart, $styleEnd - $removeStart)
            Write-Host "Removed internal mega menu styles from $($_.Name)"
        }
    }

    if ($newContent -ne $content) {
        [System.IO.File]::WriteAllText($_.FullName, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($_.Name)"
    }
}
