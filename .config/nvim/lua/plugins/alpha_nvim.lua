return {
    {
        'goolord/alpha-nvim',
        config = function()
            require 'alpha'.setup(require 'alpha.themes.dashboard'.config)
        end
    }, {
    {
        'goolord/alpha-nvim',
        dependencies = {
            'nvim-mini/mini.icons',
            'nvim-lua/plenary.nvim'
        },
        config = function()
            require 'alpha'.setup(require 'alpha.themes.theta'.config)
        end
    },
}

};
