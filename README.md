# obp-gen-mobi
A tool to convert EPUBs to AZW3

## Usage

### Installation

This script depends on `calibre`. On Debian (or Debian-based distributions) this package can be installed via $ `apt-get install calibre`.

### Usage
$ `bash run -i input_file.epub -o output_file.azw3`

### Clean-up

`bash clean [-y]`

would remove temporary files (untracked files and folders stored in the _obp-gen-mobi_ folder). The script asks for the user's confirmation before removing the files, but if you are running this as part of a script you might want to use the`-y` flag to bypass the confirmation.

## Docker

### Installation

Clone the repo and build the image with $ `docker build . -t openbookpublishers/obp-gen-mobi`.

### Usage

```bash
docker run --rm \
           -v /path/to/local.epub:/ebook_automation/epub_file.epub \
	   -v /path/to/output:/ebook_automation/output \
           openbookpublishers/obp-gen-mobi \
	   bash run -i input_file.epub -o output_file.azw3
```

## Thoth Wrapper (Optional)

The [Thoth](https://thoth.pub/) wrapper stored at `./src/thoth_wrapper.py` would:

 - Run the conversion scripts;
 - Query the metadata repository to retrieve the ISBN of the edition;
 - Add ISBN to the AZW3 file metadata.

Run the container with:

```bash
docker run --rm \
	   --user `id -u`:`id -g` \
	   -v `pwd`/input/file.epub:/ebook_automation/epub_file.epub \
	   -v `pwd`/output/obp-gen-mobi:/ebook_automation/output \
	   openbookpublishers/obp-gen-mobi \
           thoth_wrapper.py --doi 10.11647/obp.0275
```

## Contributing

Pull requests are welcome.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
