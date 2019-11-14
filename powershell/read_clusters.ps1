#!/usr/bin/pwsh

$VCENTER = $args[0]
$USER = $args[1]
$PASS = $args[2]
$PATHPREFIX = $args[3]

If ($VCENTER -eq $Null) { Exit }
If ($USER -eq $Null) { Exit }
If ($PASS -eq $Null) { Exit }
If ($PATHPREFIX -eq $Null) { $PATHPREFIX = "." }

Connect-VIServer -Server $VCENTER -User $USER -Password $PASS | Out-Null

# Cluster ermitteln
$CLUSTER = Get-Cluster | ForEach { $_.Name }
Write-Host "TYPE = 'VMware vSphere'"
Write-Host "NAME = '$CLUSTER'"

#Disconnect-VIServer -Confirm $false -Force -Server bs
#Disconnect-VIServer -Server * -Force
