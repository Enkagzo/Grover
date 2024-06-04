/// # Sample
/// Getting started
///
/// # Description
/// This is a minimal Q# program that can be used to start writing Q# code.
namespace Grover {

    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Arrays;
    open Microsoft.Quantum.Math;

    // @EntryPoint()
    operation Main() : Result[] {
        let nMarkedItems = 1;

        let nQubits = 3;
        let nTotalItems = 2^nQubits;
        let nIterations = 1;

        use qs = Qubit[nQubits];
        return GroverSearch(qs, PhaseOracleAlternating, nIterations);
    }

    operation GroverSearch (qs : Qubit[], phaseOracle : (Qubit[] => Unit), nIterations : Int) : Result[] {
        ApplyToEachCA (H, qs);
        for idxIteration in 1..nIterations {
            phaseOracle(qs);
            ReflectionAboutUniform(qs);
        }
        let result = MeasureEachZ(qs);
        ResetAll(qs);
        return result;
    }

    // function ComputeNIterations (nMarkedItems : Int, nTotalItems : Int) : Int {
    //     return 1
    // }

    operation ReflectionAboutUniform (qs : Qubit[]) : Unit {
        within {
            ApplyToEachCA (H, qs);
        } apply {
            ReflectionAboutAllZero(qs);
        }
    }

    operation ReflectionAboutAllZero (qs : Qubit[]) : Unit {
        within {
            ApplyToEachCA (X, qs);
        } apply {
            ReflectionAboutAllOne(qs);
        }
    }

    operation ReflectionAboutAllOne (qs : Qubit[]) : Unit {
        Controlled Z (Most(qs), Tail(qs));
    }

    operation MarkingOracleAlternating (qs : Qubit[], aux : Qubit) : Unit {
        within {
            ApplyToEachCA (X, qs[0..2..Length(qs)-1]);
        } apply {
            Controlled X (qs, aux);
        }
    }

    operation PhaseOracleFromMarkingOracle (qs : Qubit[], markingOracle : ((Qubit[], Qubit) => Unit)) : Unit {
        use aux = Qubit();
        within {
            X(aux);
            H(aux);
        } apply {
            markingOracle(qs, aux);
        }
        let zeroResult = MResetZ(aux);
    }

    operation PhaseOracleAlternating (qs : Qubit[]) : Unit {
        PhaseOracleFromMarkingOracle (qs, MarkingOracleAlternating);
    }

}
