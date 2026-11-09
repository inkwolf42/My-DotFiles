return {
  "MagicDuck/grug-far.nvim",
  cmd = "GrugFar",
  keys = {
    {
      "<leader>sr",
      function()
        require("grug-far").open({ transient = true })
      end,
      mode = { "n", "x" },
      desc = "Search and Replace",
    },
    {
      "<leader>sw",
      function()
        require("grug-far").open({
          transient = true,
          prefills = { search = vim.fn.expand("<cword>") },
        })
      end,
      desc = "Replace word under cursor",
    },
  },
  opts = { headerMaxWidth = 80 },
}