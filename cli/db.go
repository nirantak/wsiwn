package cli

import (
	"github.com/nirantak/wsiwn/api"
	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(dbCmd)
	dbCmd.AddCommand(dbInitCmd)
}

var dbCmd = &cobra.Command{
	Use:   "db",
	Short: "Database commands",
	Long:  `Setup and manage the database`,
}

var dbInitCmd = &cobra.Command{
	Use:   "init",
	Short: "Initialize the database",
	Long:  `Download the data files and initialize the database`,
	Run: func(cmd *cobra.Command, args []string) {
		api.SetupDataFiles()
	},
}
