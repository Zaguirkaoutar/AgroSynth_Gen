from pathlib import Path

def test_required_directories_exist():
    for path in ["configs", "data", "src", "scripts", "outputs", "reports", "docs"]:
        assert Path(path).is_dir()
