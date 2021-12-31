package cli

import (
	"github.com/nirantak/wsiwn/api"
	"github.com/spf13/cobra"
)

func init() {
	rootCmd.AddCommand(dbCmd)
	dbCmd.AddCommand(dbFetchCmd)
	dbCmd.AddCommand(dbInitCmd)
}

var dbCmd = &cobra.Command{
	Use:   "db",
	Short: "Database commands",
	Long:  `Setup and manage the database`,
}

var dbFetchCmd = &cobra.Command{
	Use:   "fetch",
	Short: "Download data from IMDb",
	Long:  `Download and Extract the data files from IMDb`,
	Run: func(cmd *cobra.Command, args []string) {
		api.SetupDataFiles()
	},
}

var dbInitCmd = &cobra.Command{
	Use:   "init",
	Short: "Initialize the database",
	Long:  `Initialize the local WSIWN database`,
	Run: func(cmd *cobra.Command, args []string) {
		api.SetupDB()
	},
}
