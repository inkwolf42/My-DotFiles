return {
	"stevearc/conform.nvim",
	event = { "BufWritePre" },
	cmd = { "ConformInfo" },
	keys = {
		{
			"<leader>pf",
			function()
				require("conform").format({ async = true, lsp_format = "fallback" })
			end,
			mode = "",
			desc = "Format buffer",
		},
	},
	opts = {
		formatters_by_ft = {
			sql = { "sql_formatter" }, -- underscore: conform's name
			go = { "gofumpt" },
			lua = { "stylua" },
			python = { "ruff_organize_imports", "ruff_fix", "ruff_format" },
			javascript = { "prettierd", "prettier", stop_after_first = true },
			typescript = { "prettierd", "prettier", stop_after_first = true },
		},
		formatters = {
			sql_formatter = {
				prepend_args = { "--language", "sqlite" },
			},
		},
		format_on_save = function(bufnr)
			local ft = vim.bo[bufnr].filetype
			return {
				timeout_ms = 100,
				lsp_format = ft == "sql" and "never" or "fallback",
			}
		end,
	},
}
