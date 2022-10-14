# =========================================================
# Author:  Dennis Perrone
# Github:  https://www.github.com/dennis-perrone
# Purpose: Create skeleton directory for college classes.
# =========================================================

using namespace System.Management.Automation.Host

$weeks = 10
$user = $env:username
# $home is a built in variable for the home directory.
$date = Get-Date -UFormat "%Y-%m-%d"
$main_dir = "$home\Documents\college"

Clear-Host
write-host $date


# Reference;; https://adamtheautomator.com/powershell-menu/
# Reference for dynamic menu: https://stackoverflow.com/questions/35705021/powershell-dynamic-menu-from-array
function New-Menu {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Title
    )

    do {
        Write-Host "`n$Title"
        Write-Host $("=" * $Title.Length)
        # $menu = 'Prod', 'Test', 'Dev', 'test4'
        $menu = 'Administrative', 'Classes'
        $index = 1
        foreach ($i in $menu) {
            # Write-Host "$index. $i servers"
            Write-Host "$index. $i"
            # Write-Host "`t$index. $i servers"
            $index++
        }
        Write-Host "$index. 'q to quit'"
        Write-Host $("=" * $Title.Length)
        $choice = Read-Host "`nPlease select option"
        }
        until (($choice -eq '1') -or ($choice -eq '2') -or ($choice -eq 'Q') )
        switch ($choice) {
           '1'{
            Administrative
            Write-Host "`nCompleteted admin tasks ..."
           }
           '2'{
            Classes
            Write-Host "`nCompleted $i environment ..."
           }
           '3'{
               Write-Host "`nYou have selected a Dev Environment"
            }
            'Q'{
              Return
           }
        }
}

function Administrative {
    Write-Host "This is from the Hello function."
    Write-Host $main_dir
}

function Classes {
    Write-Host "Creating class structure ..."
    $folders = 'syllabus', 'discussions', 'notes', 'projects'
    $weeks = 10
    $semester = Read-Host "Enter semester (ex. Fall 2021 would be F2021)"
    $class = Read-Host "Enter class (ex. IFSM441)"
    $discussions = Read-Host "Enter number of discussions per week"
    $responses = Read-Host "Enter number of responses required per week"
    # Write-Host $semester.ToLower()
    # Write-Host $semester.ToUpper()
    $index = 1
    # Reference: https://devblogs.microsoft.com/powershell-community/determine-if-a-folder-exists/
    # Reference: https://www.educba.com/powershell-if-not/
    if (-Not ( Test-Path -Path $main_dir\classes )) {
        New-Item $main_dir\classes -ItemType Directory
    }
    
    if (-Not ( Test-Path -Path $main_dir\classes\$semester-$class )) {
        foreach ($i in $folders) {
            $FolderIndex = "{0:d2}" -f $index
            # Write-Host $FolderIndex-$i
            New-Item $main_dir\classes\$semester-$class\$FolderIndex-$i -ItemType Directory
            $index++
        }
    }
    else {
        Write-Host $class.ToUpper() "for" $semester.ToUpper() "is already present."
    }
    
    foreach ($i in @(1..$weeks)) {
        $folder = $folders[1].TrimEnd()
        $week_num = '{0:d2}' -f $i
        Write-Host "Creating discussion post templates for week $week_num ..."
        foreach ($discussion_num in @(1..$discussions)) {
            discussion_template
            foreach ($response_num in @(1..$responses)) {
            $response_num++
            }
        $discussion_num++        
        }
    $i++   
    }
}

function discussion_template {
    # Reference: https://www.configjon.com/create-and-print-a-word-document-with-powershell/
    # Create a new Word document
    $word = New-Object -ComObject Word.Application
    $Document = $Word.Documents.Add()
    $Selection = $Word.Selection

    # Format the Word document
    # Set margins
    $Selection.PageSetup.LeftMargin = 36
    $Selection.PageSetup.RightMargin = 36
    $Selection.PageSetup.TopMargin = 36
    $Selection.PageSetup.BottomMargin = 36
    # Set Font styles

    #Title
    $Selection.Style = 'Heading 1'
    $Selection.Font.Size = '13'
    #$Selection.ParagraphFormat.Alignment = 1
    $Selection.TypeText("Week $('{0:d2}' -f $i) Discussion $('{0:d2}' -f $discussion_num) - Initial Post")
    $Selection.TypeParagraph()

    #Body
    $Selection.Style = 'Heading 2'
    $Selection.Font.Size = '12'
    #$Selection.ParagraphFormat.Alignment = 1
    $Selection.TypeText("Discussion Prompt:")
    foreach ( $type in @(1..3)) {
        $Selection.TypeParagraph()
    }
    $Selection.Style = 'Heading 2'
    $Selection.Font.Size = '12'
    #$Selection.ParagraphFormat.Alignment = 1
    $Selection.TypeText("Discussion Response:")
    $Selection.TypeParagraph()
    $Selection.TypeParagraph()
 
    # Loops for discussion responses
    foreach ($response_num in @(1..$responses)) {
        # Response Heading
        $Selection.InsertNewPage()
        $Selection.Style = 'Heading 1'
        $Selection.Font.Size = '13'
        $Selection.TypeText("Week $('{0:d2}' -f $week_num) Discussion $('{0:d2}' -f $discussion_num) - Response $('{0:d2}' -f $response_num)")
        $Selection.TypeParagraph()
        # Response Text
        $Selection.Style = 'Heading 2'
        $Selection.Font.Size = '12'
        $Selection.TypeText("Discussion Response:")
        #$Selection.ParagraphFormat.Alignment = 1
        $Selection.TypeParagraph()

    }

    #Save the Word document
    $SaveLoc = "$main_dir\classes\$semester-$class\02-$folder\week-$('{0:d2}' -f $i)-discussion-$('{0:d2}' -f $discussion_num).docx"
    $Document.SaveAs([ref]$SaveLoc,[ref]$SaveFormat::wdFormatDocument)
    $word.Quit()
}

New-Menu -Title 'College Directory Skeleton Builder'