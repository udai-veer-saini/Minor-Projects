Public Class Form1
    Private Sub btnSelectColor_Click(sender As Object, e As EventArgs) Handles btnSelectColor.Click
        Dim colorDialog As New ColorDialog()

        If colorDialog.ShowDialog() = DialogResult.OK Then
            Dim selectedColor As Color = colorDialog.Color

            Dim colorBox As New Panel()
            colorBox.BackColor = selectedColor
            colorBox.Width = 30
            colorBox.Height = 30
            colorBox.Margin = New Padding(5)

            flpPalette.Controls.Add(colorBox)
        End If
    End Sub
    Private Sub btnClearPalette_Click(sender As Object, e As EventArgs) Handles btnClearPalette.Click
        flpPalette.Controls.Clear()
    End Sub
End Class
