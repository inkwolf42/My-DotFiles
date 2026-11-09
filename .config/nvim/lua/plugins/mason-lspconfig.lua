return {
	"williamboman/mason-lspconfig.nvim",
	dependencies = {
		"williamboman/mason.nvim",
		"neovim/nvim-lspconfig",
	},
	config = function()
		local mason_lspconfig = require("mason-lspconfig")

		mason_lspconfig.setup({
			handlers = {
				function(server_name)
					require("lspconfig")[server_name].setup({})
				end,

				["lua_ls"] = function()
					require("lspconfig").lua_ls.setup({
						settings = {
							Lua = {
								diagnostics = {
									globals = { "vim" }, -- Fix the annoying "Undefined global 'vim'" warning
								},
							},
						},
					})
				end,
			},
		})
	end,
}
