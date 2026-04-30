$c = Get-Content -Path 'templates\index-2.html' -Raw
$c = $c -replace 'href="about-us-v2.html"', 'href="{{ url_for(''catch_all'', filename=''about-us-v2.html'') }}"'
Set-Content -Path 'templates\index-2.html' -Value $c
Write-Host "Replaced about-us-v2.html"
