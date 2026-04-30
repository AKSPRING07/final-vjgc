$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

# New Compact About Us
$compactAbout = @'
										<ul class="dropdown-menu about-dropdown compact-dropdown">
											<li><a href="{{ url_for(''catch_all'', filename=''about-us-v2.html'') }}">About Vijayalakshmi Group</a></li>
											<li><a href="{{ url_for(''catch_all'', filename=''about-us-v1.html'') }}">Mission & Vision</a></li>
											<li><a href="{{ url_for(''catch_all'', filename=''service-v1.html'') }}">Leadership and Awards</a></li>
										</ul>
'@

# New Compact Newsroom
$compactNews = @'
										<ul class="dropdown-menu news-dropdown compact-dropdown">
											<li><a href="{{ url_for(''catch_all'', filename=''media-release.html'') }}">Media Releases</a></li>
											<li><a href="{{ url_for(''catch_all'', filename=''media-kit.html'') }}">Media Kit</a></li>
										</ul>
'@

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    $changed = $false

    # 1. Update About Us (Replace mega structure with compact)
    # Target the entire About Us li and its dropdown
    $aboutRegex = '(?s)<li class="nav-item dropdown mega-dropdown">\s*<a[^>]*>About Us\s*</a>\s*<ul class="dropdown-menu about-dropdown">.*?</ul>\s*</li>'
    if ($content -match $aboutRegex) {
        $newAboutLi = "<li class=`"nav-item dropdown`">`n										<a class=`"nav-link dropdown-toggle`" href=`"#`" role=`"button`"`n											data-bs-toggle=`"dropdown`" data-bs-auto-close=`"outside`"`n											aria-expanded=`"false`">About Us`n										</a>`n$compactAbout`n									</li>"
        $content = $content -replace $aboutRegex, $newAboutLi
        $changed = $true
    }

    # 2. Update Newsroom (Replace mega structure with compact)
    $newsRegex = '(?s)<li class="nav-item dropdown mega-dropdown">\s*<a[^>]*>Newsroom\s*</a>\s*<ul class="dropdown-menu news-dropdown">.*?</ul>\s*</li>'
    if ($content -match $newsRegex) {
        $newNewsLi = "<li class=`"nav-item dropdown`">`n										<a class=`"nav-link dropdown-toggle`" href=`"#`" role=`"button`"`n											data-bs-toggle=`"dropdown`" data-bs-auto-close=`"outside`"`n											aria-expanded=`"false`">Newsroom`n										</a>`n$compactNews`n									</li>"
        $content = $content -replace $newsRegex, $newNewsLi
        $changed = $true
    }

    if ($changed) {
        Write-Host "Updating $($file.Name)..."
        $content = $content.Replace("''", "'")
        [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    }
}

Write-Host "All About Us and Newsroom menus converted to compact dropdowns."
