package main

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

func main()  {
  r := gin.Default()

  r.GET("/login", func(ctx *gin.Context) {
    ctx.JSON(http.StatusOK, gin.H{
      "message": "ok",
    })
  })
  r.Run()
}
