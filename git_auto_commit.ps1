# Ajouter tous les fichiers
git add .

# Trouver le dernier fichier ajouté (peu importe le dossier)
$lastFile = git diff --cached --name-only | Select-Object -Last 1

if ($lastFile) {
    # Extraire le nom sans extension
    $filename = [System.IO.Path]::GetFileNameWithoutExtension($lastFile.ToString())
    # Faire le commit avec le message demandé
    git commit -m "RootMe - $filename"
    # Pousser sur le dépôt distant
    git push
}
else {
    Write-Host "Aucun fichier ajouté."
}