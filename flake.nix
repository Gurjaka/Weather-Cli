{
  description = "Weather Cli Project";

  inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      py = pkgs.python312Packages;
  in
  {
    devShells.${system}.default  =
    pkgs.mkShell
      {
      buildInputs =  with pkgs; [
        python3
        py.pip
        py.requests
        py.simplejson
        py.simple-term-menu
      ];

      shellHook = ''
        echo "Hello World"
      '';
    };
  };
}