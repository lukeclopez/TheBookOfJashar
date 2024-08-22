GAME_SITE = https://lukeclopez.github.io/TheBookOfJashar
QR_CODE_COLOR = 533400

# Default target to display help message
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  generate-game   - Generate game files"
	@echo "  generate-sitemap - Generate sitemap file"


.PHONY: generate-game
generate-game:
	@echo "Generating game files..."
	@echo "Coming soon..."

.PHONY: generate-sitemap
generate-sitemap:
	@echo "Generating sitemap file..."
	tree ./pages -f -i -o sitemap --noreport
	python ./scripts/format-sitemap.py $(GAME_SITE)

.PHONY: generate-qr-codes
generate-qr-codes:
	@echo "Generating QR codes..."
	python ./scripts/generate-qr-codes.py sitemap 300 '#$(QR_CODE_COLOR)' True

.DEFAULT_GOAL := help
