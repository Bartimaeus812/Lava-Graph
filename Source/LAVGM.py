#Setup Graph Screen
StoreGDB 1
BackgroundOff
GridOff
AxesOff
ExprOff
ClrDraw
#Initialize data matrix
{13,20→dim([A]
#If data in [A] outside of range, make 0
For(A,1,13
    For(B,1,20)
    If min([A](A,B)≠{0,1,2,3
        0→[A](A,B
    End
End
Lbl M
#Display level from [A]
For(A,1,12
    For(B,1,20
        Text(12A-3,12B+2,sub("^I-O",[A](A,B)+1,1
    End
End
#Set pos YX
1→A
Ans→B
#Repeat until press enter
Repeat K=105
    getKey→K
    #If press key, display level at pos
    If Ans
        Text(12A-3,12B+2,sub("^I-O",[A](A,B)+1,1
    #If press clear, exit
    If K=45
        Goto E
    #YX movement
    min(12,max(1,A+sum(List(Ans={25,34→A
    min(20,max(1,B+sum(List(K={24,26→B
    #If not press enter, display cursor
    If K≠105
        Text(12A-3,12B+2,"X
    #If press 0,1,2,or 3, store 0,1,2,or 3 in [A]
    If max(K={102,92,93,94
        (K=92)+2(K=93)+3(K=94→[A](A,B
End
#Initialize player data
{0→L₁
#Put all Y,X positions of win in L1
For(A,1,12
    For(B,1,20)
        If 3=[A](A,B
            augment(L₁,{A,B→L₁
    End
End
#If no win positions, return to editor
If 1=dim(L₁
    Goto M
ClrDraw
Text(9,12,"SELECT WIN POSITION: <-,->
Pause 
ClrDraw
RecallPic 1
#Set L1 pos 2 (1 is invalid)
2→A
#Repeat until press enter
Repeat K=105
    getKey→K
    #If press key, display win character
    If Ans
        Text(12L₁(A)-3,12L₁(A+1)+2,"O
    #Movement between L1 Y,X elements
    min(dim(L₁)-1,max(2,A+2sum(List(Ans={24,26→A
    #Display cursor
    Text(12L₁(A)-3,12L₁(A+1)+2,"X
End
#Selected Win Y,X store in L1
{L₁(A+1),L₁(A+2→L₁
StorePic 1
ClrDraw
Text(9,12,"Select start position
Pause 
ClrDraw
RecallPic 1
#Set pos YX
1→A
Ans→B
#Repeat until press enter
Repeat K=105
    getKey→K
    #If press key, display level at pos
    If Ans
        Text(12A-3,12B+2,sub("^I-O",[A](A,B)+1,1
    #Movement YX
    min(12,max(1,A+sum(List(Ans={25,34→A
    min(20,max(1,B+sum(List(K={24,26→B
    #Display Cursor
    Text(12A-3,12B+2,"X
    #If press clear, return to editor
    If K=45
        Goto M
End
#If selected pos is non-air, return to editor
If [A](A,B
    Goto M
#Rebuild L1 as {Start Y, Start X, Win Y, Win X}
augment({A,B},L₁→L₁
ClrDraw
Text(9,12,"Lava  placement:  Lower,  Upper,
Text(21,12,"Start
Pause 
ClrDraw
RecallPic 1
#Set pos YX
1→A
Ans→B
#Set L2 index
0→C
#Initialize lava data
{Ans→L₂
Lbl L
#Next L2 index
1+C→C
#Repeat until press enter
Repeat K=105
    getKey→K
    #If press key, display lava
    If Ans
        Text(12A-3,14,"^
    #Move Y
    min(12,max(0,A+sum(List(Ans={25,34→A
    #Display Cursor
    Text(12A-3,14,"X
End
#Store Selected Y in lava data at index
A→L₂(C
#If not last index choose new Y pos
If C≠3
    Goto L
ClrDraw
Text(9,14,"Lava starts going:"
Text(21,14,"1 = Up"
Text(33,14,"2 = Down"
#Repeat until press 1 or 2
Repeat max(K={92,93
    getKey→K
End
#1->0->up 2->1->down
sum(List(K={92,93→L₂(4
#Initialize display data
" →Str1
#Initialize starts list
{0→L₃
ClrDraw
#Add correctly spaced characters to display data
For(A,1,12)
    #start index of current row
    length(Str1→L₃(A+1
    For(B,1,20
        Text(12A-3,12B+2,"X
        If not([A](A,B
            Str1+"      →Str1
        If 1=[A](A,B
            Str1+"[]→Str1
        If 2=[A](A,B
            Str1+"  -→Str1
        If 3=[A](A,B)
            Str1+"  O→Str1
    End
End
length(Str1→L₃(14
#initialize starts and lengths matrix
[[0→[B]
{2,13→dim([B]
#Fix starts
L₃+1→L₃
#Store starts in matrix, then store lengths
For(A,1,2
    For(B,2,13
        L₃(B→[B](A,B-1
    End
    #Calculate lengths
    List(L₃→L₃
End
ClrDraw
#Display Level from display data and starts-lengths matrix
For(A,1,12
    Text(12A-3,12,sub(Str1,[B](1,A),[B](2,A
End
Pause 
#Exit
Lbl E
ClrDraw
RecallGDB 1
ClrHome
"