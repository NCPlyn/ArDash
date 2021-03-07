using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ardashtest
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(!String.IsNullOrWhiteSpace(comboBox1.Text) && !String.IsNullOrWhiteSpace(comboBox2.Text))
            {
                Form1.SerialPortCommunicator.SerialPort.PortName = comboBox1.Text;
                Form1.SerialPortCommunicator.SerialPort.BaudRate = Int32.Parse(comboBox2.Text);
                Form1.SerialPortCommunicator.SerialPort.Open();
                this.Close();
            }
            else
            {
                MessageBox.Show("Please select port and baud rate!", "Error");
            }
            
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            comboBox1.Items.Clear();
            comboBox1.Items.AddRange(System.IO.Ports.SerialPort.GetPortNames());
        }
    }
}
