#Setup Graph Screen
StoreGDB 1
BackgroundOff
GridOff
AxesOff
ExprOff
#initialize level index
0→S
#Get max level index in variable L
prgmLAVGP
#Set initial keycode and level index to 1
1→K:Ans→S
#repeat until level index reaches end of level list or player press clear key
Repeat S>L or K=45
    #get level at index S
    prgmLAVGP
    #setup graph screen again
­    164→Ymin
    264→Xmax
    0→Ymax
    Ans→Xmin
    #set var H
    0→H
    Lbl M
    #read level again?
    prgmLAVGP
    #draw level
    ClrDraw
    For(A,1,12
        Text(12A-3,12,sub(Str1,[B](1,A),[B](2,A
    End
    #get level again?
    prgmLAVGP
    #if lava going (up/down)?
    If L₂(4
    Then
        #draw lava from lower to current
        For(C,L₂(1),L₂(3),­1
            Text(12C-3,12,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        End
    End
    #draw current lava
    Text(12L₂(3)-3,12,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #Ans is not 1, likely 0
    Ans→D
    #keycode
    Ans→K
    1→G
    #starting YX
    L₁(1→A
    L₁(2→B
    #Repeat until Y matches current lava or player press clear or player YX matches Win YX
    Repeat A=L₂(3) or K=45 or A=L₁(3) and B=L₁(4
        #Lava Counter Variable ++
        E+1→E
        #If lava counter matches max timer val
        If Ans=L₂(5
        Then
            #If lava current stalled, spawn at lower
            If ­1=L₂(3
            Then
                #store lower into current
                L₂(1)→L₂(3
                #display
                Text(12Ans-3,12,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            End
            #If upper lava matches current lava, go down
            If L₂(2)=L₂(3
                #set lava direction down
                1→L₂(4
            #If lava direction down and lava current matches lava lower
            If (L₂(1)=L₂(3))L₂(4
            Then
                #set lava direction up
                0→L₂(4
                #set lava current to stall
­                1→L₂(3
            End
            #If lava current is not stalled and lava direction up
            If (­1≠L₂(3))not(L₂(4
                #lava current --
                L₂(3)-1→L₂(3
            #If lava direction down
            If L₂(4
            Then
                L₂(3
                #Display lava current
                Text(12Ans-3,12,sub(Str1,[B](1,Ans),[B](2,Ans
                #Lava current ++
                Ans+1→L₂(3
            End
            #If lava current stalled
            If ­1=L₂(3)
            Then
                L₂(1
                #Display lava lower
                Text(12Ans-3,12,sub(Str1,[B](1,Ans),[B](2,Ans
            #if lava current not stalled
            Else
                #display lava current
                Text(12L₂(3),12,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            End
            #reset lava counter variable
            0→E
        End
        getKey→K
        #If press key, clear player
        If Ans
            Text(C,D,"      "
        #Y pos go down if player on platform and press down
        A+(K=34)(2=[A](A+1,B→A
        #Move left/right according to left/right arrows, clamped between 1 and 20, STAYS IN ANS
        min(20,max(1,B+sum(List(K={24,26
        #If not wall at new Pos, store move value
        If 1≠[A](A,Ans
            Ans→B
        #Set clear X
        12B→D
        #If press up and on floor/wall/platform
        If (K=25)(A=12 or max([A](A+1,B)={1,2
        Then
            #Jump up to 3 spaces as walls/ceiling allow
            For(F,1,3)
                #If not at ceiling
                If A>1
                Then
                    #If not at wall
                    If 1≠[A](A-1,B
                    Then
                        #Move position up
                        A-1→A
                    End
                End
            End
            #Set gravity
­            1→G
        End
        #Set new clear Y
        12A-3→C
        #gravity ++
        1+G→G
        #If on floor or standing on non-air, set gravity
        If A=12 or [A](A+1,B
            1→G
        #If gravity matches 2 (and standing on air)
        If Ans=2
        Then
            #clear position
            Text(C,D,"      
            #If at platform
            If 2=[A](A,B
                #display platform
                Text(C,D,"  -
            #Move player down
            A+1→A
            #Move clear Y down
            C+12→C
            #Set gravity
            1→G
        End
        #Display player
        Text(C,D+2,"X
    End
    #If player Y matches lava current, rebuild level
    If A=L₂(3
        Goto M
    #else, move to next level
    1+S→S
End
#reset graph screen
ClrDraw
AxesOn 
ZStandard
RecallGDB 1
ClrHome
"