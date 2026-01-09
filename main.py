import json
import argparse
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from data_models import Cube
from utils import visualize_single, visualize_all_grid

from utils import generate_settings, chain_to_triangles


def build_midpoint_indices():
    """Build mapping from midpoint coordinates to edge indices."""
    cube_empty = Cube()
    midpoint_indices = {}
    for index, edge in enumerate(cube_empty.edges):
        midpoint = cube_empty.vertices[edge[0]].midpoint(
            cube_empty.vertices[edge[1]])
        midpoint_indices[(midpoint.x, midpoint.y, midpoint.z)] = index
    return midpoint_indices


def generate_all_single_visualizations(settings):
    """Generate individual visualization files for each configuration."""
    print("Generating individual configuration visualizations...")
    for config, cube, polygon, midpoints, chains in settings:
        visualize_single(config, cube, midpoints, chains)
    print("Individual visualizations complete.")


def write_output_files(settings):
    """Write LUT data to various formats (Python, JSON, etc)."""
    print("Writing output files...")
    midpoint_indices = build_midpoint_indices()
    
    # Collect all triangle data
    lut_data = {}
    lut_list = []
    
    for config, cube, polygon, midpoints, chains in settings:
        midpoint_indices_list = []
        for chain in chains:
            triangles = chain_to_triangles(chain, cube)
            for triangle in triangles:
                for point in triangle:
                    midpoint_indices_list.append(midpoint_indices[point])
        
        # Add terminator -1 if we have any triangles
        if midpoint_indices_list:
            midpoint_indices_list.append(-1)
            
        lut_data[str(config)] = midpoint_indices_list
        lut_list.append(midpoint_indices_list)
    
    # Write Python file
    with open("LUTs/LUT.py", "w") as f:
        f.write("LUT = [\n")
        for i, data in enumerate(lut_list):
            f.write(f"    {data},  # Config: {i}\n")
        f.write("]\n")
    
    # Write JSON file
    with open("LUTs/LUT.json", "w") as f:
        json.dump(lut_data, f, indent=2)
    
    print("Output files written to LUTs/")


def generate_full_visualization(settings):
    """Generate the full 16x16 grid visualization."""
    print("Generating full grid visualization...")
    visualize_all_grid(settings)
    print("Full visualization complete.")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate marching cubes configurations and visualizations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                           # Run all operations
  python main.py --draw-grid               # Only draw the full grid
  python main.py --draw-all-singles        # Only draw individual configs
  python main.py --write-files             # Only write LUT files
  python main.py --draw-grid --write-files # Draw grid and write files
        """
    )
    
    parser.add_argument(
        "--draw-grid", 
        action="store_true", 
        help="Generate the full 16x16 grid visualization"
    )
    
    parser.add_argument(
        "--draw-all-singles", 
        action="store_true", 
        help="Generate individual visualization files for each configuration"
    )
    
    parser.add_argument(
        "--write-files", 
        action="store_true", 
        help="Write LUT data to Python and JSON files"
    )
    
    parser.add_argument(
        "--config", 
        type=int, 
        metavar="N",
        help="Generate visualization for a specific configuration (0-255)"
    )
    
    args = parser.parse_args()
    
    # If no flags specified, run all operations
    if not any([args.draw_grid, args.draw_all_singles, args.write_files, args.config is not None]):
        args.draw_grid = True
        args.draw_all_singles = True
        args.write_files = True
    
    return args


def main():
    """Main function - orchestrates all operations."""
    args = parse_args()
    
    print("Generating marching cubes configurations...")
    settings = generate_settings()
    
    # Run specific configuration if requested
    if args.config is not None:
        if 0 <= args.config <= 255:
            config, cube, polygon, midpoints, chains = settings[args.config]
            print(f"Generating visualization for configuration {args.config}...")
            visualize_single(config, cube, midpoints, chains)
            print(f"Configuration {args.config} visualization complete.")
        else:
            print(f"Error: Configuration must be between 0 and 255, got {args.config}")
        return
    
    # Run selected operations
    operations_run = []
    
    if args.draw_all_singles:
        generate_all_single_visualizations(settings)
        operations_run.append("individual visualizations")
    
    if args.write_files:
        write_output_files(settings)
        operations_run.append("LUT files")
    
    if args.draw_grid:
        generate_full_visualization(settings)
        operations_run.append("grid visualization")
    
    if operations_run:
        print(f"Complete! Generated: {', '.join(operations_run)}")
    else:
        print("No operations selected.")


if __name__ == "__main__":
    main()
