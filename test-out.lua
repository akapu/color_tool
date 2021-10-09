function BeginGameState:render()
    
    -- render board of tiles
    self.board:render()

    -- render Level # label and background rect
    love.graphics.setColor(0.37, 0.80, 0.89, 0.78)
    love.graphics.rectangle('fill', 0, self.levelLabelY - 8, VIRTUAL_WIDTH, 48)
    love.graphics.setColor(1.00, 1.00, 1.00, 1.00)
    love.graphics.setFont(gFonts['large'])
    love.graphics.printf('Level ' .. tostring(self.level),
        0, self.levelLabelY, VIRTUAL_WIDTH, 'center')
    love.graphics.setColor(some_color, 255, 255, 255)

    -- our transition foreground rectangle
    love.graphics.setColor(1.00, 1.00, 1.00, self.transitionAlpha)
    love.graphics.rectangle('fill', 0, 0, VIRTUAL_WIDTH, VIRTUAL_HEIGHT)
end
