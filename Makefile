GAME_SITE = https://lukeclopez.github.io/TheBookOfJashar
QR_CODE_COLOR = 533400

# Default target to display help message
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  generate-game   - (Re)generate all game files from data files"
	@echo "  generate-sitemap - Generate sitemap file"
	@echo "  generate-qr-codes - Generate QR codes"


.PHONY: generate-game
generate-game:
	@echo "Generating game files..."
	python ./scripts/generate-blessing-cards-and-pages.py
	python ./scripts/generate-city-cards-and-pages.py
	python ./scripts/generate-direction-cards-and-pages.py
	python ./scripts/generate-event-cards-and-pages.py
	python ./scripts/generate-tribe-tablets.py

	@echo "Generating combination files..."
	python ./scripts/generate-card-grid.py
	python ./scripts/generate-tribe-tablet-grid.py

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
