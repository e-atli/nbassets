#!/usr/bin/pwsh

Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2] | Out-Null

# Cluster ermitteln
$CLUSTERS = Get-Cluster

Foreach ($CLUSTER in $CLUSTERS) {
  Write-Host "CLUSTER = '$CLUSTER'"
  
  $VMS = Get-VM -Location $CLUSTER

  Foreach ($VM in $VMS) {
    #Write-Host "CLUSTER = '$CLUSTER'"
    $NAME = $VM.Name
    Write-Host "NAME = '$NAME'"

    $VCPUS = $VM.NumCpu
    Write-Host "VCPUS = '$VCPUS'"

    $MEMORY = $VM.MemoryMB
    Write-Host "MEMORY = '$MEMORY'"

    $DISK = [math]::round((Get-HardDisk -vm $VM | Measure-Object -Sum CapacityGB).Sum)
    Write-Host "DISK = '$DISK'"

    $STATUS = $VM.PowerState
    Write-Host "STATUS = '$STATUS'"
 
    $ROLE = ((Get-TagAssignment -Entity $VM -Category 'Role')).Tag.Name
    IF ($ROLE) { Write-Host "ROLE = '$ROLE'" }

    Write-Host ""
  }

Write-Host ""
}
