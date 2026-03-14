import shutil
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

from eve_static_data.helpers.sde_info import SdeInfo, load_sde_info_from_zipfile


def unpack(
    input_path: Path, output_path: Path, use_build_number: bool = True
) -> tuple[Path, SdeInfo]:
    """Unpack the static data.

    Unzip the input file and save the unpacked data to the output path.

    If use_build_number is True, the unpacked data will be saved to
    `<output_path>/<build_number>/`. Otherwise, it will be saved to `<output_path>/`.

    Checks for the presence of the _sde.jsonl file in the unpacked files. If the file is not
    found, raises a FileNotFoundError.


    Args:
        input_path: The path to the static data jsonl zip file.
        output_path: The path to the directory where the unpacked data should be saved.
        use_build_number: Whether to use the build number from the _sde.jsonl file to create the output directory.


    Returns:
        A tuple containing the path to the directory where the unpacked data is saved and the SdeInfo object.
    """
    if not input_path.is_file():
        raise FileNotFoundError(f"Input path {input_path} is not a file.")
    if input_path.suffix != ".zip":
        raise ValueError(f"Input file {input_path} is not a zip file.")
    if output_path.exists() and not output_path.is_dir():
        raise FileExistsError(
            f"Output path {output_path} already exists and is not a directory."
        )
    sde_info = load_sde_info_from_zipfile(input_path)
    build_number = sde_info.get("buildNumber")
    if build_number is None:  # type: ignore
        raise ValueError(
            f"Build number not found in _sde.jsonl file in the zip file {input_path}."
        )
    unpack_dir = output_path / str(build_number) if use_build_number else output_path
    if unpack_dir.exists() and not unpack_dir.is_dir():
        raise FileExistsError(
            f"Output directory {unpack_dir} already exists and is not a directory."
        )
    with TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(input_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
        sde_info_file = Path(temp_dir) / "_sde.jsonl"
        if not sde_info_file.exists():
            raise FileNotFoundError(
                f"_sde.jsonl file not found in the unzipped SDE data at {temp_dir}. Is this a valid SDE zip file?"
            )

        unpack_dir.mkdir(parents=True, exist_ok=True)
        for file in Path(temp_dir).iterdir():
            if file.is_file():
                target_file = unpack_dir / file.name
                if target_file.exists():
                    raise FileExistsError(
                        f"Target file {target_file} already exists. Cannot move processed data to {target_file}"
                    )
                shutil.move(file, target_file)
        return unpack_dir, sde_info
