{ pkgs ? import <nixpkgs> {} }:
let
  python = pkgs.python3;
  pythonPackages = python.pkgs;

  # Define salat dependency manually from PyPI
  salat = pythonPackages.buildPythonPackage rec {
    pname = "salat";
    version = "1.1.0";
    src = pythonPackages.fetchPypi {
      inherit pname version;
      sha256 = "sha256-vJxpSDzPGs8TA179TXNyJW3A9CWPfnFub7uU55UjFB8=";
      # Replace this with the actual hash from nix build error (see below)
    };

    format = "setuptools";
    doCheck = false;
  };

in
  pythonPackages.buildPythonPackage rec {
    pname = "nsalah";
    version = "0.2.0";
    src = ./.;
    format = "setuptools";

    propagatedBuildInputs = with pythonPackages; [
      setuptools
      salat
    ];

    doCheck = false;

    meta = with pkgs.lib; {
      description = "A python program to print the next salah and remaining time.";
      homepage = "https://github.com/pxlman/next-salah";
      license = licenses.mit;
    };
  }
