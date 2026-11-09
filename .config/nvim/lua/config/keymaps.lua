local keymap = vim.keymap.set

-- Better window navigation (Ctrl + h/j/k/l)
keymap("n", "<C-h>", "<C-w>h", { desc = "Go to left window" })
keymap("n", "<C-j>", "<C-w>j", { desc = "Go to lower window" })
keymap("n", "<C-k>", "<C-w>k", { desc = "Go to upper window" })
keymap("n", "<C-l>", "<C-w>l", { desc = "Go to right window" })

-- Clear search highlights easily
keymap("n", "<leader>nh", ":nohlsearch<CR>", { desc = "Clear search highlights" })

-- Shortcuts
keymap("n", "<leader>ee", "oif err != nil{<CR>}<ESC>Oreturn err<ESC>", { desc = "Print If err statement for go" })
keymap(
	"n",
	"<leader>bs",
	'O#! /usr/bin/env bash<CR><CR>set -o pipefail  # Set the status code take the one that failed not the last one<CR>set -e # Exit if error happened<CR>set -u # Exit if use variable that dose not exists<CR><CR>if [[ "${TRACE-0}" == "1" ]]; then set -o xtrace; fi<CR><CR><ESC>',
	{ desc = "Starting Line for bash script" }
)
keymap("n", '<leader>"', 'F$i"<ESC>eea"')
-- surond the selected segment with paires
local pairs_map = {
	["("] = { "(", ")" },
	[")"] = { "(", ")" },
	["["] = { "[", "]" },
	["]"] = { "[", "]" },
	["{"] = { "{", "}" },
	["}"] = { "{", "}" },
	["<"] = { "<", ">" },
	[">"] = { "<", ">" },
	['"'] = { '"', '"' },
	["'"] = { "'", "'" },
	["`"] = { "`", "`" },
}

vim.keymap.set("x", "<leader>ss", function()
	local key = vim.fn.getcharstr()
	local p = pairs_map[key]
	if not p then
		return
	end -- Esc, Alt combos, unknown keys: do nothing

	local mode = vim.fn.mode()
	vim.cmd("normal! \27") -- leave visual mode so '< and '> are set
	local s = vim.api.nvim_buf_get_mark(0, "<")
	local e = vim.api.nvim_buf_get_mark(0, ">")
	local srow, scol, erow = s[1] - 1, s[2], e[1] - 1
	local line = vim.api.nvim_buf_get_lines(0, erow, erow + 1, false)[1] or ""
	local ecol = math.min(e[2] + 1, #line)
	if e[2] < #line and vim.str_utf_end then
		ecol = math.min(e[2] + 1 + vim.str_utf_end(line, e[2] + 1), #line)
	end
	if mode == "V" then
		scol, ecol = 0, #line
	end

	-- closer first so the start position doesn't shift
	vim.api.nvim_buf_set_text(0, erow, ecol, erow, ecol, { p[2] })
	vim.api.nvim_buf_set_text(0, srow, scol, srow, scol, { p[1] })
end, { desc = "Surround selection" })
