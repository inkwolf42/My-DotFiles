return {
  "mfussenegger/nvim-lint",
  event = { "BufReadPre", "BufNewFile", "BufWritePost" }, -- Trigger linting on open and save

  dependencies = {
      "williamboman/mason.nvim",
      "rshkarin/mason-nvim-lint", -- The bridge plugin
    },

  config = function()
    local lint = require("lint")

    

    require("mason-nvim-lint").setup({
        automatic_installation = true, 
      })

    -- Create an autocmd to automatically trigger linting
    local lint_augroup = vim.api.nvim_create_augroup("lint", { clear = true })
    vim.api.nvim_create_autocmd({ "BufEnter", "BufWritePost", "InsertLeave" }, {
      group = lint_augroup,
      callback = function()
        -- Only run linting if the file belongs to an active, supported buffer type
        lint.try_lint()
      end,
    })
  end,
}
