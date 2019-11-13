#!/usr/bin/pwsh

Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2] | Out-Null

# Cluster ermitteln
$CLUSTER = Get-Cluster | ForEach { $_.Name }
Write-Host "TYPE = 'VMware vSphere'"
Write-Host "NAME = '$CLUSTER'"

#Disconnect-VIServer -Confirm $false -Force -Server bs
#Disconnect-VIServer -Server * -Force
