#!/usr/bin/pwsh

$VCENTER = $args[0]
$USER = $args[1]
$PASS = $args[2]
$PATHPREFIX = $args[3]

If ($VCENTER = $Null) { Exit }
If ($USER = $Null) { Exit }
If ($PASS = $Null) { Exit }
If ($PATHPREFIX = $Null) { $PATHPREFIX = "." }

# Verbinde zum vCenter
Write-Host $args[0]
Write-Host "$VCENTER"
Write-Host "$USER"
Write-Host "$PASS"
Write-Host "$PATHPREFIX"

exit 
Connect-VIServer -Server "$VCENTER" -User "$USER" -Password "$PASS" | Out-Null

# Cluster ermitteln
$CLUSTERS = Get-Cluster

Foreach ($CLUSTER in $CLUSTERS) {
  "CLUSTER = '$CLUSTER'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py
  
  $VMS = Get-VM -Location $CLUSTER

  Foreach ($VM in $VMS) {
    $NAME = $VM.Name
    "NAME = '$NAME'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append
    
    $VCPUS = $VM.NumCpu
    "VCPUS = '$VCPUS'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append

    $MEMORY = $VM.MemoryMB
    "MEMORY = '$MEMORY'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append

    $DISK = [math]::round((Get-HardDisk -vm $VM | Measure-Object -Sum CapacityGB).Sum)
    "DISK = '$DISK'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append

    $STATUS = $VM.PowerState
    "STATUS = '$STATUS'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append
 
    $ROLE = ((Get-TagAssignment -Entity $VM -Category 'Role')).Tag.Name
    IF ($ROLE) { "ROLE = '$ROLE'" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append }

    "" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append
  }

"" | Out-File -FilePath $PATHPREFIX/vm_$CLUSTER.py -Append
}

