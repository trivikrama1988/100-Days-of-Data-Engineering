# setup.ps1 - Windows PowerShell setup script

Write-Host "Setting up 100 Days of Data Engineering Web Interface..." -ForegroundColor Green

# Create main directories
$directories = @(
    "days",
    "projects",
    "phases",
    "templates",
    "scripts",
    "api"
)

foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "Created: $dir" -ForegroundColor Cyan
    }
}

# Create assets subdirectories
$assetDirs = @(
    "assets",
    "assets/css",
    "assets/js",
    "assets/images"
)

foreach ($dir in $assetDirs) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "Created: $dir" -ForegroundColor Cyan
    }
}

# Initialize npm
if (!(Test-Path "package.json")) {
    npm init -y
    Write-Host "Initialized npm package.json" -ForegroundColor Green
}

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
npm install --save-dev live-server

# Create basic files
$files = @{
    "index.html" = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>100 Days of Data Engineering</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <h1>100 Days of Data Engineering</h1>
        <p>Loading...</p>
    </div>
    <script src="app.js"></script>
</body>
</html>
"@

    "styles.css" = @"
/* Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    background: #f8fafc;
    color: #1e293b;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

h1 {
    color: #2563eb;
    margin-bottom: 1rem;
}
"@

    "app.js" = @"
// Main Application
console.log('100 Days of Data Engineering Web App');

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    console.log('App loaded');

    // Check if user has visited before
    if (!localStorage.getItem('de_visited')) {
        localStorage.setItem('de_visited', new Date().toISOString());
        console.log('First visit recorded');
    }
});
"@

    "scripts/generate-days.js" = @"
// Day page generator
console.log('Day page generator will be implemented here');

// This will generate HTML files for all 100 days
// based on exercises.md
"@
}

foreach ($file in $files.GetEnumerator()) {
    $filePath = $file.Key
    $content = $file.Value

    if (!(Test-Path $filePath)) {
        New-Item -Path $filePath -ItemType File -Force
        Set-Content -Path $filePath -Value $content
        Write-Host "Created: $filePath" -ForegroundColor Cyan
    }
}

# Update package.json with scripts
$packageJsonPath = "package.json"
if (Test-Path $packageJsonPath) {
    $packageJson = Get-Content $packageJsonPath | ConvertFrom-Json

    # Add scripts if they don't exist
    if (!$packageJson.scripts) {
        $packageJson.scripts = @{}
    }

    $packageJson.scripts.start = "live-server --port=8080"
    $packageJson.scripts.build = "node scripts/generate-days.js"

    $packageJson | ConvertTo-Json -Depth 10 | Set-Content $packageJsonPath
    Write-Host "Updated package.json with scripts" -ForegroundColor Green
}

Write-Host "`n✅ Setup complete!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Run: npm start" -ForegroundColor Cyan
Write-Host "2. Open http://localhost:8080 in your browser" -ForegroundColor Cyan
Write-Host "3. Start building your day pages" -ForegroundColor Cyan