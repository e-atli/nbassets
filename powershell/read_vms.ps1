#!/usr/bin/pwsh

# Prüfe ob 3 Variablen übergeben wurden
For ($i = 0; $i -lt 3; $i++)
     {
        If ($args[$i] = $Null) { Exit }
     }

If ($args[3]) {
  $PATHPREFIX="$args[3]"
  }
Else {
  $PATHPREFIX="."
  }

# Verbinde zum vCenter
Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2] | Out-Null

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

