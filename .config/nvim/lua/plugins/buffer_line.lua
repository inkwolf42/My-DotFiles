return {
    "akinsho/bufferline.nvim",
    version = "*",
    event = "VeryLazy",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    opts = function()
        local opts = {
            options = {
                mode = "tabs",
                diagnostics = "nvim_lsp",
                always_show_bufferline = false, -- hide when only one buffer is open
            },
        }
        -- use catppuccin colors if it's the active colorscheme
        if (vim.g.colors_name or ""):find("catppuccin") then
            opts.highlights = require("catppuccin.special.bufferline").get_theme()
        end
        return opts
    end,
    keys = {
        { "<S-h>",      "<cmd>BufferLineCyclePrev<cr>",   desc = "Prev buffer" },
        { "<S-l>",      "<cmd>BufferLineCycleNext<cr>",   desc = "Next buffer" },
        { "<leader>bp", "<cmd>BufferLineTogglePin<cr>",   desc = "Pin buffer" },
        { "<leader>ba", "<cmd>BufferLineCloseOthers<cr>", desc = "Close other buffers" },
        { "<leader>bc", "<cmd>bd<cr>",                    desc = "Close other buffers" },
        { "<leader>bb", "<cmd>BufferLinePick<cr>",        desc = "Pick buffer" },
    },
}
