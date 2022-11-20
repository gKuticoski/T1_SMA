import java.util.ArrayList;

public class Fila {
    private ArrayList<Double> numbers = new ArrayList<>();
    private ArrayList<Double> tempoEstados = new ArrayList<>();
    private final int A = 8121;
    private final int C = 978;
    private final int M = 134456;
    private double seed;
    private int totalNumerosGerados;
    private int qtdServidores;
    private int tamAtual;
    private double tempoAcc=0.0;
    private double tMinChegada, tMaxChegada;
    private double tMinServico, tMaxServico;

    public Fila() {
        this.seed = 663877;
        this.totalNumerosGerados = 0;
    }

    private void generate() {
        seed = (((this.seed * this.A) + this.C) % this.M);
        this.numbers.add(seed / this.M);
    }

    private random_time(int a, int b) {
        this.totalNumerosGerados++;
        int randomNumber = (b - a) * random.random() + a
        return randomNumber;
    }

    private chegada(int novoTempo) {
        int tempoDecorrido = this.tempoEstados.get(tamAtual) + novoTempo - this.tempoAcc;
        this.tempoEstados.add(tamAtual, tempoDecorrido);
        this.tempoAcc = novoTempo;

        if(this.tamAtual < this.tamMax){
            this.tamAtual++;
            double tempo;
            if(this.tamAtual <= this.qtdServidores){
                App.agendaFila.add(this.id);
                App.agendaTipo.add("saida");
            }
        }
    }
}