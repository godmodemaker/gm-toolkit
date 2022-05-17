def pbShowCommands(helptext,commands,index=0)
  ret = -1
  helpwindow = @sprites["helpwindow"]
  helpwindow.visible = true
  using(cmdwindow = Window_CommandPokemonColor.new(commands)) {
    cmdwindow.z     = @viewport.z+1
    cmdwindow.index = index
    pbBottomRight(cmdwindow)
    helpwindow.resizeHeightToFit(helptext,Graphics.width-cmdwindow.width)
    helpwindow.text = helptext
    pbBottomLeft(helpwindow)
    loop do
      Graphics.update
      Input.update
      cmdwindow.update
      self.update
      if Input.trigger?(Input::B)
        pbPlayCancelSE
        ret = -1
        break
      elsif Input.trigger?(Input::C)
        pbPlayDecisionSE
        ret = cmdwindow.index
        break
      end
    end
  }
  return ret
end

cmd = 0
loop do
  cmd=@scene.pbShowCommands(_INTL("Select option:"),[_INTL("Option 1"),_INTL("Option 2"),_INTL("Option 3")],cmd)
  if cmd==-1
    break
  elsif cmd==0
    kernel.pbDisplay(_INTL("Option 1"))
    #Code here
  elsif cmd==1
    kernel.pbDisplay(_INTL("Option 2"))
    #Code here
  elsif cmd==2
    kernel.pbDisplay(_INTL("Option 3"))
    #Code here
  end
end