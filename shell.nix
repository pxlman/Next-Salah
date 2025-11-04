let 
pkgs = import <nixpkgs> {};
nsalah = pkgs.callPackage ./default.nix {};
in
pkgs.mkShell {
  buildInputs = [
    nsalah
    ];
}
