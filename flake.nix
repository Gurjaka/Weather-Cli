{
  description = "Weather Cli Project";

  inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      py = pkgs.python3.pkgs;
  in
  {
    devShells.${system}.default =
    pkgs.mkShell
      {
      packages =  with pkgs; [
        python3
        fish
        py.pip
        py.requests
        py.simplejson
      ];
      
      shellHook = ''
        exec fish
      '';
    };
  };
}
