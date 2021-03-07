using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using System.Security;

namespace Ardashtest
{
    public partial class Form1 : Form
    {
        private static SerialPort _serialPort = new SerialPort();
        public static class SerialPortCommunicator
        {
            public static SerialPort SerialPort
            {
                get { return _serialPort; }
                set { _serialPort = value; }
            }
        }
        public Form1()
        {
            InitializeComponent();
        }
        int innit = 0;
        string curdir = System.AppDomain.CurrentDomain.BaseDirectory;
        private void Button3_Click(object sender, EventArgs e)
        {
            if (!String.IsNullOrWhiteSpace(TextBox1.Text))
            {
                isInnit();
                TextBox7.AppendText(Environment.NewLine+ "    if(serIN == '" + TextBox1.Text + "'):" + Environment.NewLine);
                TextBox7.AppendText("        os.system('" + TextBox3.Text + "')");
            }
            else
            {
                MessageBox.Show("Please fill out 'On button'! (number from 1-X)", "Error");
            }
        }
        public void isInnit()
        {
            if (innit == 0)
            {
                TextBox7.AppendText("from pynput.keyboard import Key, Controller" + Environment.NewLine + "keyboard = Controller()" + Environment.NewLine + "import os" + Environment.NewLine + Environment.NewLine + "def ifFunc(serIN, bcolors):");
                innit = 1;
            }
        }
        public string needUvozov(TextBox textbox)
        {
            if(textbox.Text.Length == 1)
            {
                return ("'");
            }
            else
            {
                return ("");
            }
        }
        
        private void Button4_Click(object sender, EventArgs e)
        {
            if (!String.IsNullOrWhiteSpace(TextBox1.Text))
            {
                isInnit();
                TextBox7.AppendText(Environment.NewLine + "    if(serIN == '" + TextBox1.Text + "'):" + Environment.NewLine);
                for (int i = 0; i < TextBox6.Lines.Length; i++)
                {
                    TextBox7.AppendText("        " + TextBox6.Lines[i]);
                }
            }
            else
            {
                MessageBox.Show("Please fill out 'On button'! (number from 1-X)", "Error");
            }
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            if (!String.IsNullOrWhiteSpace(TextBox1.Text))
            {
                isInnit();
                TextBox7.AppendText(Environment.NewLine + "    if(serIN == '" + TextBox1.Text + "'):" + Environment.NewLine);
                if (String.IsNullOrWhiteSpace(TextBox4.Text) && String.IsNullOrWhiteSpace(TextBox5.Text))
                {
                    TextBox7.AppendText("        keyboard.tap(" + needUvozov(TextBox2) + TextBox2.Text + needUvozov(TextBox2) + ")");
                }
                else if (String.IsNullOrWhiteSpace(TextBox5.Text) && !String.IsNullOrWhiteSpace(TextBox4.Text))
                {
                    TextBox7.AppendText("        keyboard.press(" + needUvozov(TextBox2) + TextBox2.Text + needUvozov(TextBox2) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.press(" + needUvozov(TextBox4) + TextBox4.Text + needUvozov(TextBox4) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.release(" + needUvozov(TextBox4) + TextBox4.Text + needUvozov(TextBox4) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.release(" + needUvozov(TextBox2) + TextBox2.Text + needUvozov(TextBox2) + ")");
                }
                else if (!String.IsNullOrWhiteSpace(TextBox5.Text) && !String.IsNullOrWhiteSpace(TextBox4.Text))
                {
                    TextBox7.AppendText("        keyboard.press(" + needUvozov(TextBox2) + TextBox2.Text + needUvozov(TextBox2) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.press(" + needUvozov(TextBox4) + TextBox4.Text + needUvozov(TextBox4) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.press(" + needUvozov(TextBox5) + TextBox5.Text + needUvozov(TextBox5) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.release(" + needUvozov(TextBox5) + TextBox5.Text + needUvozov(TextBox5) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.release(" + needUvozov(TextBox4) + TextBox4.Text + needUvozov(TextBox4) + ")" + Environment.NewLine);
                    TextBox7.AppendText("        keyboard.release(" + needUvozov(TextBox2) + TextBox2.Text + needUvozov(TextBox2) + ")");
                }
            }
            else
            {
                MessageBox.Show("Please fill out 'On button'! (number from 1-X)", "Error");
            }
        }

        private void Button5_Click(object sender, EventArgs e)
        {
            innit = 0;
            TextBox7.Text = "";
        }
        protected override bool ProcessDialogKey(Keys keyData)
        {
            if (keyData == Keys.Tab)
            {
                if (TextBox6.Focused == true) {
                    TextBox6.AppendText("    ");
                }
                if (TextBox7.Focused == true)
                {
                    TextBox7.AppendText("    ");
                }
                return true;
            }
            return base.ProcessDialogKey(keyData);
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            if (File.Exists(curdir + "bindings.py")) 
            {
                System.IO.File.Copy(curdir + "bindings.py", curdir + "bindings.py.old", true);
            }
            FileStream fcreate = File.Open(curdir + "bindings.py", FileMode.Create);
            StreamWriter x = new StreamWriter(fcreate);
            for (int i = 0; i < TextBox7.Lines.Length; i++)
            {
                x.WriteLine(TextBox7.Lines[i]);
            }
            x.Close();
            _serialPort.Close();
            MessageBox.Show("New bindings file written, old file archived." + Environment.NewLine + "Serial connection between Arduino was closed." + Environment.NewLine + "To use ArDash, please start it again as it was killed when starting this app.", "Info");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2(); 
            f2.ShowDialog();
        }

        public void _serialPort_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            string line = _serialPort.ReadExisting();
            this.BeginInvoke(new LineReceivedEvent(LineReceived), line);
        }

        private delegate void LineReceivedEvent(string line);
        private void LineReceived(string line)
        {
            TextBox1.Text = line;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            _serialPort.DtrEnable = true;
            _serialPort.DataReceived += _serialPort_DataReceived;
        }

        private void LinkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("https://github.com/NCPlyn/ArDash/wiki/How-to-use-Binding-creator-app");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Process proc = new Process();
            proc.StartInfo.FileName = "python.exe";
            proc.StartInfo.Arguments = curdir + "ArDash.py";
            proc.StartInfo.UseShellExecute = true;
            proc.StartInfo.Verb = "runas";
            proc.Start();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (innit == 1 && !String.IsNullOrWhiteSpace(textBox8.Text))
            {
                TextBox7.AppendText(Environment.NewLine + "        print(bcolors.CYAN+'[INFO]'+bcolors.ENDC+' " + textBox8.Text + "')");
            }
            else
            {
                MessageBox.Show("Please, make entry first ", "Error");
            }   
        }
    }
}
