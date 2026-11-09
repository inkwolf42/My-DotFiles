return {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    cmd = "NeoTree",
    keys = {
        { "<leader>e", "<cmd>Neotree toggle<CR>", { desc = "Toggle file explorer" } }
    },
    dependencies = {
        "nvim-lua/plenary.nvim",
        "nvim-tree/nvim-web-devicons",
        "MunifTanjim/nui.nvim",
    },
    init = function()
        vim.api.nvim_create_autocmd("BufEnter", {
            group = vim.api.nvim_create_augroup("Neotree_start_directory", { clear = true }),
            once = true,
            callback = function()
                if package.loaded["neo-tree"] then return end
                local stats = vim.uv.fs_stat(vim.fn.argv(0))
                if stats and stats.type == "directory" then
                    require("neo-tree")
                end
            end,
        })
    end,
    config = function()
        require("neo-tree").setup({
            filesystem = {
                use_libuv_file_watcher = true,
                scan_mode = "shallow",
                hijack_netrw_behavior = "open_default",
                filtered_items = {
                    hide_dotfiles = false, hide_gitignored = true
                }
            },
            enable_git_status = false,
            enable_diagnostics = false,
            window = {
                mappings = {
                    ["<CR>"] = "open",
                    ["o"] = "open",
                    ["t"] = "open_tabnew",
                    ["<Esc>"] = "close_window",
                }
            }
        })
    end,
}
